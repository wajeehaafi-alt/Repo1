// Test JavaScript File for Folder 3 - Dashboard
class Dashboard {
    constructor() {
        this.data = [];
        this.init();
    }
    
    init() {
        console.log("Testing Folder 3 - Dashboard JavaScript");
        this.loadData();
    }
    
    loadData() {
        this.data = [
            { id: 1, name: "Item 1" },
            { id: 2, name: "Item 2" },
            { id: 3, name: "Item 3" }
        ];
        console.log("Data loaded:", this.data);
    }
}

const dashboard = new Dashboard();

