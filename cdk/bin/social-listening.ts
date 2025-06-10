import * as cdk from 'aws-cdk-lib';
import { SocialListeningStack } from '../lib/social-listening-stack';

const app = new cdk.App();
new SocialListeningStack(app, 'SocialListeningStack');