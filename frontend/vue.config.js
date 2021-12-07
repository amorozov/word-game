// vue.config.js

/**
 * @type {import('@vue/cli-service').ProjectOptions}
 */
 module.exports = {
    // настройки...
    outputDir: "build/word-game-frontend",
    devServer: {
        overlay: {
            warnings: false,
            errors: true
        },
        proxy: {
            '^/api': {
                target: 'http://localhost:8080',
                ws: true,
                changeOrigin: true
            }
        }
    }
  }
  