import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [react()],
    server: {
        proxy: {
            '/api/service1': 'http://localhost:8001',
            '/api/service2': 'http://localhost:8002'
        }
    }
})
