pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
	            sh 'make lint'
              }
            }
            stage('Deps') {
                steps {
    	            sh 'make deps'
                  }
                }
            stage('Test') {
                steps {
    	            sh 'make test'
                  }
                }
                stage('Testxunit') {
                steps {
                    sh 'make test_xunit || true'
                    step([$class: 'XUnitBuilder',
                        thresholds: [
                            [$class: 'SkippedThreshold', failureThreshold: '0'],
                            [$class: 'FailedThreshold', failureThreshold: '1']],
                        tools: [[$class: 'JUnitType', pattern: 'test_results.xml']]])
                  }
          }
        }
}
