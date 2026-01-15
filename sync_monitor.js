// Sync monitor for tracking workflow operations
class SyncMonitor {
    constructor() {
        this.events = [];
        this.isActive = false;
    }
    
    start() {
        this.isActive = true;
        console.log('Sync monitor started');
    }
    
    logEvent(event) {
        this.events.push({
            ...event,
            timestamp: new Date().toISOString()
        });
    }
    
    getStats() {
        return {
            totalEvents: this.events.length,
            isActive: this.isActive
        };
    }
}

const monitor = new SyncMonitor();
monitor.start();
monitor.logEvent({ type: 'initialized', message: 'Monitor ready' });

