public class Main {
    public static void main(String[] args) {
        Simulation simulation = new Simulation(100, 10, 0.1, 1, 1,2,true);
        for(int i=0; i<10000; i++) {
            simulation.simulate();
        }
    }
}