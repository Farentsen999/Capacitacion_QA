# Capacitación QA Automation - Roadmap Personal

Este repositorio es una una bitácora técnica de mi formación como QA Automation. En este README documento el progreso diario, desde los fundamentos de scripting hasta la creación de frameworks robustos y escalables.

## Tecnologías Principales
* Lenguaje: Python 3.14.2
* Framework: Playwright (Python)
* Patrón de Diseño: Page Object Model (POM)
* Metodología: BDD (Gherkin) & Data-Driven Testing (DDT)
* Control de Versiones: Git

---

## Proyectos Destacados

  ### 1. SauceDemo E2E Framework (Fase 1: Finalizada)
  Framework de automatización para el flujo de compra completo en `saucedemo.com` para todos los productos.
    Desafíos superados:
      * Manejo de Importaciones Circulares en Python.
      * Implementación de Smart Waits y Web-First Assertions (`expect`).
      * Configuración de Evidencia Automática: Captura de Video y Tracing interactivo.
      * Estructuración de requerimientos mediante archivos `.feature` (Gherkin).

---

## Roadmap de Aprendizaje

  ### Fase 0: Fundamentos (dias 1-14)
  - [x] Configuración de entorno y primer test.
  - [x] Repaso uso de estructuras de datos en python (diccionarios y listas).
  - [x] Repaso estructuras de control de repetición en python (ciclos for y while)
  - [x] Implementación de un motor de reglas para validar una base de datos simulada.
  - [x] Repaso POO con python (clase, estado y comportamiento).
  - [x] Repaso general de conceptos e instalación de herramientas (Playwright y Git)
  - [x] Implementación del primer test con Playwright (práctica de busqueda web en https://duckduckgo.com)
  - [x] Test de caracteristicas usando asserts (practica en http://books.toscrape.com)
  - [x] Test de login (práctica en https://automationexercise.com/login).
  - [x] Test de con dialog (práctica en https://automationexercise.com/contact_us)
  - [x] Test con esperas dinámicas (práctica en http://the-internet.herokuapp.com/dynamic_loading/1)
  - [x] Test con extracción de tablas (práctica en https://the-internet.herokuapp.com/challenging_dom)
  - [x] Test para de flujo de compra repasar los conceptos aprendidos (práctica en https://www.saucedemo.com/)
  
  ### Fase 1: Aplicación de POM (Días 15-21)
  - [x] Refractoring del test de flujo de compra (implementación de POM).
  - [x] Gherkin e historias de usuario (descripción del flujo de compra en base a historias de usuario).
  - [x] Gestión de esperas inteligentes y aserciones resilientes.
  - [x] Configuración de Git y GitHub.
  - [x] Generación de trazas y reportes de error.
  - [x] Documentación técnica y Git Flow.
  - [x] Aplicar DDT al test de flujo de compra.
  
  ### Fase 2: Escenarios Reales y Flujos Complejos (Días 8+) 
  - [ ] Automatización de flujos de Registro y Autenticación en `automationexercise.com`.
  - [ ] Manejo de Pop-ups, IFrames y carga de archivos.
  - [ ] Integración de **PyTest** como motor de pruebas.

---

## Cómo ejecutar los tests

  ### Prerrequisitos:
  * Python 3.10 o superior
  * Git instalado
  
  ### Configuración del Entorno:
  1. Clonar el repositorio e ingresar en el
    git clone https://github.com/Farentsen999/Capacitacion_QA.git
    cd .../Capacitacion_QA
  
  3. Crear entorno virtual
    python -m venv venv
  
  4. Activar entorno virtual
    En Windows:
      .\venv\Scripts\activate
    En Linux/Mac:
      source venv/bin/activate
  
  5. Instalar dependencias del proyecto
    pip install -r requirements.txt
  
  6. Instalar binarios de los navegadores de Playwright
    playwright install

  ### Ejecución de Test
  cd dia15_QA_POM
  python -m test.test_saucedemo

  ### Visualización de Reportes
  playwright show-trace evidence/trace.zip
  
  
  
  
