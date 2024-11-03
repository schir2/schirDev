import {defineConfig} from 'vite';
import path from 'path';

export default defineConfig({
    build: {
        lib: {
            entry: path.resolve(__dirname, 'src/index.ts'),
            name: 'RetirementCalculator',
            fileName: 'retirement_calculator',
            formats: ['iife']
        },
        outDir: '../../js',
        rollupOptions: {
            output: {
                inlineDynamicImports: true,
                globals: {}
            }
        }
    },
    resolve: {}
});
