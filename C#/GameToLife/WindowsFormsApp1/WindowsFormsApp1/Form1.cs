using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public struct Cell
    {
        public int x;
        public int y;
        public bool life;

    }

    

    public partial class Form1 : Form
    {
        public bool LifeActive { get; private set; }

        public Form1()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer 
                | ControlStyles.AllPaintingInWmPaint 
                | ControlStyles.UserPaint, true);
            UpdateStyles();
        }

        Cell[,] Cells = new Cell[20, 20];

        private void FormPaint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            int n = 20;
            Pen p = new Pen(Color.Black, 1);
            SolidBrush Red = new SolidBrush(Color.Red);
            SolidBrush White = new SolidBrush(Color.White);

            for (int i = 0; i < n + 1; i++)
                g.DrawLine(p, 20, i*20 +20, (n + 1) * 20, i*20 +20);
            for (int j = 0; j < n + 1; j++)
                g.DrawLine(p, j*20 +20, 20, j * 20 + 20, (n + 1) * 20);

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Cells[i, j].x = i * 20 + 23;
                    Cells[i, j].y = j * 20 + 23;
                }
            }

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (Cells[i, j].life == true)
                    {
                        g.FillRectangle(Red, Cells[i, j].x, Cells[i, j].y, 17, 17);
                    }
                    else
                    {
                        g.FillRectangle(White, Cells[i, j].x, Cells[i, j].y, 17, 17);
                    }
                }
            }
            if (LifeActive == true)
            {
                
               /* Parallel.For(0, 19, i =>*/
               for(int i = 0; i < n; i++)
                   {
                       
                       /*Parallel.For(0, 19, j =>*/
                       for (int j = 0; j < n; j++)
                        {
                            
                            if (i == 0 && j == 0)
                            {
                                int potentional = 0;
                                #region
                                for (int x = 0; x < 2; x++)
                                {
                                    for (int y = 0; y < 2; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (i == 20 && j == 20)
                            {
                                int potentional = 0;
                                #region
                                for (int x = n - 1; x < n; x++)
                                {
                                    for (int y = n - 2; y < n; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (i == 0 && j == 19)
                            {
                                int potentional = 0;
                                #region
                                for (int x = 0; x < 2; x++)
                                {
                                    for (int y = n - 2; y < n; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (i == 19 && j == 0)
                            {
                                int potentional = 0;
                                #region
                                for (int x = n - 2; x < n; x++)
                                {
                                    for (int y = 0; y < 2; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (i == 0)
                            {
                                int potentional = 0;
                                #region
                                for (int x = 0; x < 2; x++)
                                {
                                    for (int y = j - 1; y < j + 1; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (i == 19)
                            {
                                int potentional = 0;
                                #region
                                for (int x = n - 2; x < n; x++)
                                {
                                    for (int y = j - 1; y < j + 1; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (j == 0)
                            {
                                int potentional = 0;
                                #region
                                for (int x = i - 1; x < i + 1; x++)
                                {
                                    for (int y = 0; y < 2; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else if (j == 19)
                            {
                                int potentional = 0;
                                #region
                                for (int x = i - 1; x < i + 1; x++)
                                {
                                    for (int y = n - 2; y < n; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                            else
                            {
                                int potentional = 0;
                                #region
                                for (int x = i - 1; x < i + 1; x++)
                                {
                                    for (int y = j - 1; y < j + 1; y++)
                                    {
                                        if (x != i && y != j)
                                        {
                                            if (Cells[x, y].life == true)
                                                potentional++;
                                        }
                                    }
                                }
                                if (potentional == 3)
                                    Cells[i, j].life = true;
                                else
                                {
                                    if (potentional < 2 || potentional > 3)
                                        Cells[i, j].life = false;
                                    else
                                    {

                                    }
                                }
                            #endregion
                        }
                        }//);
                    }//);
            }
    }
                

        

        private void TimerTick(object sender, EventArgs e)
        {
            bool temp_life = LifeActive;
            Refresh();
            LifeActive = temp_life;
        }

        private void StartLife(object sender, EventArgs e)
        {
            LifeActive = true;
        }

        private void StopLife(object sender, EventArgs e)
        {
            LifeActive = false;
        }

        private void AddLife(object sender, EventArgs e)
        {
            Random rnd = new Random();
            for (int i = 0; i < 20; i++)
            {
                int value_x = rnd.Next(0, 20);
                int value_y = rnd.Next(0, 20);
                Cells[value_x, value_y].life = true;

            }

        }

        private void DieAll(object sender, EventArgs e)
        {
            for (int i = 0; i < 20; i++)
            {
                for (int j = 0; j < 20; j++)
                {
                    Cells[i, j].life = false;
                }
            }
        }
    }
}
