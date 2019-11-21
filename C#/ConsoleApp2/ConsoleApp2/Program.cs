using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        public static int N;
        public static int[] arr1;
        public static int[] arr2;
        public static int[] arr3;
        public static int[] arr4;
        public static int[] arr5;
        public static int current_index = 0;

        public static void Main(string[] args)
        {
            Console.WriteLine("Сколько чисел будем обрабатывать?");
            Program.N = Convert.ToInt32(Console.ReadLine());
            Program.arr1 = new int[Program.N];
            Program.arr2 = new int[Program.N];
            Program.arr3 = new int[Program.N];
            Program.arr4 = new int[Program.N];
            Program.arr5 = new int[Program.N];
            for (int i = 0; i < Program.N; i++)
            {
                Program.arr1[i] = i + 2;
                Program.arr2[i] = i + 2;
                Program.arr3[i] = i + 2;
                Program.arr4[i] = i + 2;
                Program.arr5[i] = i + 2;
                Console.Write(Program.arr1[i] + " ");
            }
            Console.WriteLine();
            Console.WriteLine();

            for (int i = 0; i < Math.Sqrt(Program.N); i++)
            {
                if (Program.arr1[i] > 0)
                {
                    for (int j = i+1; j < Math.Sqrt(Program.N); j++)
                    {
                        if (Program.arr1[j] % Program.arr1[i] == 0)
                            Program.arr1[j] = 0;
                        if (Program.arr2[j] % Program.arr2[i] == 0)
                            Program.arr2[j] = 0;
                        if (Program.arr3[j] % Program.arr3[i] == 0)
                            Program.arr3[j] = 0;
                        if (Program.arr4[j] % Program.arr4[i] == 0)
                            Program.arr4[j] = 0;
                        if (Program.arr5[j] % Program.arr5[i] == 0)
                            Program.arr5[j] = 0;
                    }
                }
            }

            for (int i = 0; i < Math.Sqrt(Program.N); i++)
                Console.Write(Program.arr1[i] + " ");
            Console.WriteLine();
            Console.WriteLine();

            System.Diagnostics.Stopwatch sw = System.Diagnostics.Stopwatch.StartNew();
            for (int i = 0; i < Math.Sqrt(Program.N); i++)
            {
                if (Program.arr1[i] > 0)
                {
                    for (int j = i + 1; j < Program.N; j++)
                    {
                        if (Program.arr1[j] % Program.arr1[i] == 0)
                            Program.arr1[j] = 0;
                    }
                }
            }
            long elapsed = sw.ElapsedMilliseconds;
            Console.WriteLine("Время выполнения последовательного метода в миллисекундах: {0}", elapsed);
            for (int i = 0; i < Program.N; i++)
                Console.Write(Program.arr1[i] + " ");
            Console.WriteLine();
            Console.WriteLine("--------- К О Н Е Ц   П О С Л Е Д О В А Т Е Л Ь Н О Й   О Б Р А Б О Т К И ----------");
            Console.WriteLine();
            //------------------------- К О Н Е Ц   П О С Л Е Д О В А Т Е Л Ь Н О Й   О Б Р А Б О Т К И -----------------

            Console.WriteLine();
            Console.WriteLine("-------- Н А Ч А Л О   П Е Р В О Г О   П О Т О К О В О Г О   М Е Т О Д А  ----------");
            //------------------------- Н А Ч А Л О   П Е Р В О Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------
            System.Diagnostics.Stopwatch sw1 = System.Diagnostics.Stopwatch.StartNew();
            Parallel.For(Convert.ToInt32((Math.Sqrt(Program.N))),
                Convert.ToInt32(Math.Sqrt(Program.N) + ((Program.N - Math.Sqrt(Program.N))/3))
                ,i =>
            {

                for (int j = 0; j < Math.Sqrt(Program.N); j++)
                {
                    if (Program.arr2[i] > 0)
                    {
                        if (Program.arr2[j] > 0)
                        {
                            if (Program.arr2[i] % Program.arr2[j] == 0)
                                Program.arr2[i] = 0;
                        }
                    }
                }
            });
            
            Parallel.For(Convert.ToInt32(Math.Sqrt(Program.N) + ((Program.N - Math.Sqrt(Program.N)) / 3)),
                Convert.ToInt32(Math.Sqrt(Program.N) + (2 * (Program.N - Math.Sqrt(Program.N)) / 3))
                , i =>
                {

                    for (int j = 0; j < Math.Sqrt(Program.N); j++)
                    {
                        if (Program.arr2[i] > 0)
                        {
                            if (Program.arr2[j] > 0)
                            {
                                if (Program.arr2[i] % Program.arr2[j] == 0)
                                    Program.arr2[i] = 0;
                            }
                        }
                    }
                });

            Parallel.For(Convert.ToInt32(Math.Sqrt(Program.N) + (2 * (Program.N - Math.Sqrt(Program.N)) / 3)),
                Convert.ToInt32(Program.N)
                , i =>
                {

                    for (int j = 0; j < Math.Sqrt(Program.N); j++)
                    {
                        if (Program.arr2[i] > 0)
                        {
                            if (Program.arr2[j] > 0)
                            {
                                if (Program.arr2[i] % Program.arr2[j] == 0)
                                    Program.arr2[i] = 0;
                            }
                        }
                    }
                });
                
            long elapsed1 = sw1.ElapsedMilliseconds;
            Console.WriteLine("Время выполнения метода декомпозиции по данным в миллисекундах: {0}", elapsed1);

            for (int i = 0; i < Program.N; i++)
                Console.Write(Program.arr1[i] + " ");
            Console.WriteLine();
            Console.WriteLine("------------ К О Н Е Ц   П Е Р В О Г О   П О Т О К О В О Г О   М Е Т О Д А  ---------");
            Console.WriteLine();
            //------------------------- К О Н Е Ц   П Е Р В О Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------

            Console.WriteLine();
            Console.WriteLine("---------- Н А Ч А Л О   В Т О Р О Г О   П О Т О К О В О Г О   М Е Т О Д А  ------------");
            //------------------------- Н А Ч А Л О   В Т О Р О Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------
            Thread thread1 = new Thread(new ThreadStart(First_Part));
            Thread thread2 = new Thread(new ThreadStart(Second_Part));
            Thread thread3 = new Thread(new ThreadStart(Third_Part));

            System.Diagnostics.Stopwatch sw3 = System.Diagnostics.Stopwatch.StartNew();

            thread1.Start(); thread2.Start(); thread3.Start();

            long elapsed3 = sw3.ElapsedMilliseconds;
            Console.WriteLine("Время выполнения метода декомпозиции набора в миллисекундах: {0}", elapsed3);

            for (int i = 0; i < Program.N; i++)
                Console.Write(Program.arr3[i] + " ");
            Console.WriteLine();
            Console.WriteLine("------------ К О Н Е Ц   В Т О Р О Г О   П О Т О К О В О Г О   М Е Т О Д А  ---------");
            Console.WriteLine();
            //------------------------- К О Н Е Ц   В Т О Р О Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------

            Console.WriteLine("---------- Н А Ч А Л О   Т Р Е Т Ь Е Г О   П О Т О К О В О Г О   М Е Т О Д А  ------------");
            //------------------------- Н А Ч А Л О  Т Р Е Т Ь Е Г О    П О Т О К О В О Г О   М Е Т О Д А  -----------------

            System.Diagnostics.Stopwatch sw4 = System.Diagnostics.Stopwatch.StartNew();

            ManualResetEvent[] events =  new ManualResetEvent[Convert.ToInt32(Math.Sqrt(Program.N))];

            for (int i = 0; i < Convert.ToInt32(Math.Sqrt(Program.N)); i++)
            {
                events[i] = new ManualResetEvent(false);
                ThreadPool.QueueUserWorkItem(Run,
                new object[] { Program.arr4[i], events[i] });
            }
            WaitHandle.WaitAll(events);

            long elapsed4 = sw4.ElapsedMilliseconds;
            Console.WriteLine("Время выполнения метода пула потоков в миллисекундах: {0}", elapsed4);

            for (int i = 0; i < Program.N; i++)
                Console.Write(Program.arr4[i] + " ");

            Console.WriteLine();
            Console.WriteLine("------------ К О Н Е Ц   Т Р Е Т Ь Е Г О   П О Т О К О В О Г О   М Е Т О Д А  ---------");
            Console.WriteLine();
            //------------------------- К О Н Е Ц  Т Р Е Т Ь Е Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------

            Console.WriteLine("---------- Н А Ч А Л О   Ч Е Т В Е Р Т О Г О   П О Т О К О В О Г О   М Е Т О Д А  ------------");
            //------------------------- Н А Ч А Л О  Ч Е Т В Е Р Т О Г О    П О Т О К О В О Г О   М Е Т О Д А  -----------------

            System.Diagnostics.Stopwatch sw5 = System.Diagnostics.Stopwatch.StartNew();

            Thread thread_5_1 = new Thread(new ThreadStart(five_one));
            Thread thread_5_2 = new Thread(new ThreadStart(five_one));
            Thread thread_5_3 = new Thread(new ThreadStart(five_one));

            thread_5_1.Start();
            thread_5_2.Start();
            thread_5_3.Start();

            long elapsed5 = sw4.ElapsedMilliseconds;
            Console.WriteLine("Время выполнения метода пула потоков в миллисекундах: {0}", elapsed5);

            for (int i = 0; i < Program.N; i++)
                Console.Write(Program.arr5[i] + " ");

            Console.WriteLine();
            Console.WriteLine("------------ К О Н Е Ц   Ч Е Т В Е Р Т О Г О   П О Т О К О В О Г О   М Е Т О Д А  ---------");
            Console.WriteLine();
            //------------------------- К О Н Е Ц  Ч Е Т В Е Р Т О Г О   П О Т О К О В О Г О   М Е Т О Д А  -----------------


            Console.ReadKey();
        }

        private static void Run(object state)
        {
            object[] array = state as object[];
            int x = Convert.ToInt32(array[0]);
            ManualResetEvent ev = array[1] as ManualResetEvent;
            {
                if (x > 0)
                {
                    for (int j = Convert.ToInt32(Math.Sqrt(Program.N) + 1); j < Program.N; j++)
                    {
                        if (Program.arr4[j] > 0)
                        {
                            if (Program.arr4[j] % x == 0)
                                Program.arr4[j] = 0;
                        }
                    }
                }
            }
            ev.Set();
        }

        public static void First_Part()
        {
            for (int i = 1; i < Math.Sqrt(Program.N); i += 2)
            {
                if (Program.arr3[i] > 0)
                {
                    for (int j = Convert.ToInt32(Math.Sqrt(Program.N)) + 1; j < Program.N; j++)
                    {
                        if (Program.arr3[j] % Program.arr3[i] == 0)
                            Program.arr3[j] = 0;
                    }
                }
            }
        }

        public static void Second_Part()
        {
            for (int i = 2; i < Math.Sqrt(Program.N); i += 2)
            {
                if (Program.arr3[i] > 0)
                {
                    for (int j = Convert.ToInt32(Math.Sqrt(Program.N)) + 1; j < Program.N; j++)
                    {
                        if (Program.arr3[j] % Program.arr3[i] == 0)
                            Program.arr3[j] = 0;
                    }
                }
            }
        }

        public static void Third_Part()
        {
            for (int i = 3; i < Math.Sqrt(Program.N); i += 2)
            {
                if (Program.arr3[i] > 0)
                {
                    for (int j = Convert.ToInt32(Math.Sqrt(Program.N)) + 1; j < Program.N; j++)
                    {
                        if (Program.arr3[j] % Program.arr3[i] == 0)
                            Program.arr3[j] = 0;
                    }
                }
            }
        }

        public static void five_one()
        {
            while (current_index <= Convert.ToInt32(Math.Sqrt(Program.N)))
            {
                int i = current_index;
                current_index++;
                //lock (Program.arr5)
                {
                    if (Program.arr5[i] > 0)
                    {
                        for (int j = Convert.ToInt32(Math.Sqrt(Program.N)) + 1; j < Program.N; j++)
                        {
                            if (Program.arr5[j] % Program.arr5[i] == 0)
                                Program.arr5[j] = 0;
                        }
                    }
                    
                }
            }
        }



    }
}
