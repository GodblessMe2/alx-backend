import kue from "kue";

const queue = kue.createQueue();
const data = {
  phoneNumber: "12456789010",
  message: "This is the code to verify your account",
};

const queueName = "push_notification_code";

const job = queue.create(queueName, data).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});
