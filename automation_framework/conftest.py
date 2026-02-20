import pytest
import os
import pytest_html

# Esto obtiene la ruta de la carpeta donde vive conftest.py (dia15_QA_POM)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence")
VIDEO_DIR = os.path.join(EVIDENCE_DIR, "videos")
SCREENSHOT_DIR = os.path.join(EVIDENCE_DIR, "screenshots")
TRACE_DIR = os.path.join(EVIDENCE_DIR, "traces")

@pytest.fixture(scope="function")
def page(browser, request):
    """Fixture que gestiona video y tracing usando rutas absolutas"""
    
    # Se crean las carpetas si no existen usando la ruta absoluta
    for folder in [VIDEO_DIR, TRACE_DIR, SCREENSHOT_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    context = browser.new_context(
        record_video_dir=f"{VIDEO_DIR}/",
        viewport={'width': 1280, 'height': 720}
    )
    
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    yield page 
    
    # Teardown
    test_name = request.node.name
    context.tracing.stop(path=os.path.join(TRACE_DIR, f"trace_{test_name}.zip"))
    
    video_path = page.video.path() if page.video else None
    
    page.close()
    context.close()

    if hasattr(request.node, "rep_call") and request.node.rep_call.passed:
        if video_path and os.path.exists(video_path):
            os.remove(video_path)
    elif video_path and os.path.exists(video_path):
        final_video_name = os.path.join(VIDEO_DIR, f"fail_{test_name}.webm")
        os.rename(video_path, final_video_name)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        if report.failed:
            page = item.funcargs.get("page")
            if page:
                if not os.path.exists(SCREENSHOT_DIR):
                    os.makedirs(SCREENSHOT_DIR)
                
                screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
                page.screenshot(path=screenshot_path)
                extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra