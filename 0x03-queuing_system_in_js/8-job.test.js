const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');
const { expect } = require('chai');

describe('testing queue', () => {
    it('not an array', () => {
        const list = 'Not an array';
        const queue = kue.createQueue({ name: 'push_notification_code_test' });
        expect(
            createPushNotificationsJobs.bind(createPushNotificationsJobs, list, queue)
          ).to.throw('Jobs is not an array');
    });
});