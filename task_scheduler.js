// Task scheduler for workflow automation
class TaskScheduler {
    constructor() {
        this.tasks = [];
        this.running = false;
        this.interval = null;
    }
    
    addTask(task) {
        this.tasks.push({
            ...task,
            id: Date.now() + Math.random(),
            status: 'pending',
            createdAt: new Date()
        });
    }
    
    start(intervalMs = 5000) {
        if (this.running) {
            console.log('Scheduler already running');
            return;
        }
        
        this.running = true;
        this.interval = setInterval(() => {
            this.processTasks();
        }, intervalMs);
        
        console.log(`Task scheduler started (interval: ${intervalMs}ms)`);
    }
    
    stop() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
        this.running = false;
        console.log('Task scheduler stopped');
    }
    
    processTasks() {
        const pendingTasks = this.tasks.filter(t => t.status === 'pending');
        pendingTasks.forEach(task => {
            task.status = 'processing';
            console.log(`Processing task: ${task.id}`);
            // Task execution logic here
            task.status = 'completed';
        });
    }
    
    getStats() {
        return {
            total: this.tasks.length,
            pending: this.tasks.filter(t => t.status === 'pending').length,
            processing: this.tasks.filter(t => t.status === 'processing').length,
            completed: this.tasks.filter(t => t.status === 'completed').length
        };
    }
}

const scheduler = new TaskScheduler();
scheduler.addTask({ name: 'sync_repositories', priority: 'high' });
console.log('Task scheduler initialized');

