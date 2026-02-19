import pytest
import os

@pytest.fixture(scope="function")
def page(browser):
    """Fixture que configura el contexto con video y tracing para cada test"""
    if not os.path.exists("evidence/videos"):
        os.makedirs("evidence/videos")

    context = browser.new_context(
        record_video_dir="evidence/videos/",
        viewport={'width': 1280, 'height': 720}
    )
    
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    yield page 
    
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    context.tracing.stop(path=f"evidence/trace_{test_name}.zip")
    context.close()