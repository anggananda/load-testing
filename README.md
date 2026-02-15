# 🚀 EIS Undiksha - Load Testing Suite

This repository contains an automated performance and load testing suite for the **Executive Information System (EIS) Undiksha API**. Built with **Locust**, this suite evaluates the stability, throughput, and scalability of the backend services under various traffic conditions.

## 🏗 System Architecture Under Test

The target system is a high-performance executive dashboard backend:
* **Backend:** Go (Gin Gonic framework).
* **Database:** MongoDB (Aggregated data via ETL processes).
* **Caching:** Redis (Aggressive caching for executive KPIs).
* **Auth:** Undiksha SSO integration with **JWT (JSON Web Token)**.

## 🧪 Testing Strategies

We employ four main strategies to ensure system reliability:
1.  **Smoke Testing:** Verifies script integrity and basic server connectivity with minimal load.
2.  **Load Testing:** Simulates expected daily traffic to measure baseline performance.
3.  **Stress Testing:** Identifies the **Breaking Point** by pushing concurrency beyond limits.
4.  **Endurance (Soak) Testing:** Monitors for memory leaks or performance decay over extended periods.



## 🛠 Prerequisites

* Python 3.8+ or Docker.
* A valid **JWT Token** from Undiksha SSO.

## ⚙️ Installation & Setup

### Local Setup
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anggananda/load-testing.git](https://github.com/anggananda/load-testing.git)
    cd load-testing
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment:**
    Create a `.env` file in the root directory:
    ```env
    JWT_TOKEN=your_jwt_token_here
    ```

### Docker Setup
If you prefer Docker, you can run the suite without installing Python locally:
```bash
docker-compose up -d
