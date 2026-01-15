// Event handler for workflow automation
class EventHandler {
    constructor() {
        this.listeners = new Map();
        this.eventQueue = [];
    }
    
    on(eventType, callback) {
        if (!this.listeners.has(eventType)) {
            this.listeners.set(eventType, []);
        }
        this.listeners.get(eventType).push(callback);
    }
    
    emit(eventType, data) {
        if (this.listeners.has(eventType)) {
            this.listeners.get(eventType).forEach(callback => {
                callback(data);
            });
        }
    }
    
    processQueue() {
        while (this.eventQueue.length > 0) {
            const event = this.eventQueue.shift();
            this.emit(event.type, event.data);
        }
    }
}

const eventHandler = new EventHandler();

// Example usage
eventHandler.on('sync_complete', (data) => {
    console.log('Sync completed:', data);
});

eventHandler.on('error', (error) => {
    console.error('Error occurred:', error);
});

console.log('Event handler initialized');

