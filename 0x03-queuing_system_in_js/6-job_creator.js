const kue = require('kue');

const queue = kue.createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
    phoneNumber: 'string',
    message: 'string',
});

job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
    console.log(`Notification job completed`);
}).on('failed', () => {
    console.log(`Notification job failed`);
});

job.save();