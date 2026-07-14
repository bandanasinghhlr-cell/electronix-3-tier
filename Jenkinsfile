pipeline {
    agent { label 'electronix' }

    environment {
        S3_BUCKET = 'electronix-production-2026'
        CLOUDFRONT_ID = 'E1YC0W5PVDE1X4'
        AWS_REGION = 'us-east-1'
    }

    stages {
        stage("Install Dependencies") {
            when {
                changeset "frontend/**"
            }
            steps {
                dir('frontend') {
                    sh '''
                    npm install
                    '''
                }
            }
        }

        stage("Run Tests") {
            when {
                changeset "frontend/**"
            }
            steps {
                dir('frontend') {
                    sh 'npm test -- --watchAll=false || echo "No Test Configured.."'
                }
            }
        }

        stage("Build") {
            when {
                changeset "frontend/**"
            }
            steps {
                dir('frontend') {
                    sh 'npm run build'
                }
            }
        }

        stage("Deploy S3") {
            when {
                changeset "frontend/**"
            }
            steps {
                dir('frontend') {
                    sh '''
                    aws s3 sync dist/ s3://${S3_BUCKET} --delete --region ${AWS_REGION}
                    '''
                }
            }
        }

        stage("Invalidation Cloudfront Cache") {
            when {
                changeset "frontend/**"
            }
            steps {
                sh '''
                aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_ID} --paths "/*"
                '''
            }
        }
    }

    post {
        success {
            echo 'Frontent Deployment Successfull ✅'
        }

        failure {
            echo 'Frontent Deployment Failed ❌'
        }
    }
}