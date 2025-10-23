public class task_5_2 {
  
    String brand;
    String model;
    int year;

  
    public task_5_2(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }

   
    public static void main(String[] args) {
       
        task_5_2 myCar = new task_5_2("Toyota", "Corolla", 2020);

     
        myCar.displayDetails();
    }
}
