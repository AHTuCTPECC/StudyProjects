using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace pr2._2
{
    class Program
    {
        #region
        const int N = 100;
        const int K = 100;
        public Random random = new Random();
        static  public double[] massiv = new double[N];
        static  public double[] massiv1 = new double[massiv.Length];
        #endregion


      public static void Paral()
        {
            Stopwatch sw1 = new Stopwatch();
            sw1.Start();

            Parallel.For(0, massiv.Length / 2, i =>
            {
                massiv1[i] = Math.Pow(massiv[i], 1.789); // без усложнения 
            });
            sw1.Stop();
            TimeSpan ts1 = sw1.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts1.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void Paral1()
        {
            Stopwatch sw1 = new Stopwatch();
            sw1.Start();

            Parallel.For(massiv.Length / 2, massiv.Length, i => {

                massiv1[i] = Math.Pow(massiv[i], 1.789);
            });
            sw1.Stop();
            TimeSpan ts2 = sw1.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts2.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void Posled()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            for (int i = 0; i < massiv.Length; i++)
            {

                massiv1[i] = Math.Pow(massiv[i], 1.789);
            }
                sw.Stop();
                TimeSpan ts = sw.Elapsed;
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("Total time: {0}", ts.TotalMilliseconds);
                Console.ForegroundColor = ConsoleColor.White;
        }

      public static void ParalHard()
        {
            Stopwatch sw1 = new Stopwatch();
            sw1.Start();
            Parallel.For(0, massiv.Length / 2, i =>
            {

                for (int k = 0; k < massiv.Length; k++)
                {
                    for (int j = 0; j < K; j++)
                        massiv1[i] += Math.Pow(massiv[i], 1.789);
                }

            });
            sw1.Stop();
            TimeSpan ts1 = sw1.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts1.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void ParalelHard()
        {
            Stopwatch sw2 = new Stopwatch();
            sw2.Start();

            Parallel.For(massiv.Length / 2, massiv.Length, i => {
                for (int k = 0; k < massiv.Length; k++)
                {
                    // Обработка i-элемента
                    for (int j = 0; j < K; j++)
                        massiv1[i] += Math.Pow(massiv[i], 1.789);
                };
            });
            sw2.Stop();
            TimeSpan ts2 = sw2.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts2.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void PosledHard()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            for (int k = 0; k < massiv.Length; k++)
            {
                for (int j = 0; j < K; j++)
                    massiv1[k] += Math.Pow(massiv[k], 1.789);
            };
            sw.Stop();
            TimeSpan ts = sw.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void ParalelMaxHard()
        {
            Stopwatch sw1 = new Stopwatch();
            sw1.Start();

            Parallel.For(0, massiv.Length / 2, i =>
            {
                for (int k = 0; k < massiv.Length; k++)
                {
                    // Обработка i-элемента
                    for (int j = 0; j < k; j++)
                        massiv1[k] += Math.Pow(massiv[k], 1.789);
                } // по диапозону
            });
            sw1.Stop();
            TimeSpan ts1 = sw1.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts1.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void Paralel1MaxHard()
        {
            Stopwatch sw2 = new Stopwatch();
            sw2.Start();

            Parallel.For(massiv.Length / 2, massiv.Length, i => {
                for (int j = 0; j < massiv.Length / 2; j++)
                {
                    if (j % 2 != 0) //нечетные
                    {
                        massiv1[j] = Math.Pow(massiv[j], 1.789);
                        // Console.WriteLine(massiv1[j]);
                    }
                }
            });

            sw2.Stop();
            TimeSpan ts2 = sw2.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts2.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void PosledMaxHard()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            for (int i = 0; i < massiv.Length; i++)
            {
                for (int j = 0; j < i; j++)
                    massiv1[i] += Math.Pow(massiv[i], 1.789);
            }

            sw.Stop();
            TimeSpan ts = sw.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void ParalelCricle()
        {
            Stopwatch sw1 = new Stopwatch();
            sw1.Start();

            Parallel.For(0, massiv.Length / 2, i =>
            {
                for (int j = 0; j < massiv.Length / 2; j++)
                {
                    if (j % 2 == 0) //четные
                    {
                        massiv1[j] = Math.Pow(massiv[j], 1.789);
                    }
                }
            });

            sw1.Stop();
            TimeSpan ts1 = sw1.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts1.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

      public static void ParalelCricle1()
        {
            Stopwatch sw2 = new Stopwatch();
            sw2.Start();

            Parallel.For(massiv.Length / 2, massiv.Length, i => {
                for (int j = 0; j < massiv.Length / 2; j++)
                {
                    if (j % 2 != 0) //нечетные
                    {
                        massiv1[j] = Math.Pow(massiv[j], 1.789);
                        // Console.WriteLine(massiv1[j]);
                    }
                }
            });

            sw2.Stop();
            TimeSpan ts2 = sw2.Elapsed;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Total time: {0}", ts2.TotalMilliseconds);
            Console.ForegroundColor = ConsoleColor.White;
        }

        static void Main(string[] args)
        {

            Console.WriteLine("Паралельный и последовательный метод");
            Paral();
            Paral1();
            Posled();
            Console.WriteLine("Паралельный и последовательный метод с простым усложнением");
            ParalHard();
            ParalelHard();
            PosledHard();
            Console.WriteLine("Паралельный и последовательный метод со сложным усложнением");
            ParalelMaxHard();
            Paralel1MaxHard();
            PosledMaxHard();
            Console.WriteLine("Паралельный круговой метод");
            ParalelCricle();
            ParalelCricle1();
            Console.ReadLine();
        }
        
    }
}