function createPushNotificationsJobs(jobs, queue){
    if(!Array.isArray(jobs)){
        console.error(`Jobs is not an array`);
    }
    jobs.forEach(job => {
        const newJob = queue.create('push_notification_code_3', {
            phoneNumber: job.phoneNumber,
            message: job.message,
        });
        newJob.on('enqueue', () => {
            console.log(`Notification job created: ${newJob.id}`);
        });
        newJob.on('complete', () => {
            console.log(`Notification job ${newJob.id} completed`);
        });
        newJob.on('failed', () => {
            console.log(`Notification job ${newJob.id} failed: ERROR`);
        });
        newJob.save();
    });
}

module.exports = createPushNotificationsJobs;