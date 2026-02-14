using System;

class Program
{
    static void Main()
    {
        Console.Write("Напряжение: ");
        int u = int.Parse(Console.ReadLine());

        Console.Write("Сопротивление: ");
        int r = int.Parse(Console.ReadLine());

        Console.WriteLine($"Сила тока: {u / (double)r} ");
    }
}
