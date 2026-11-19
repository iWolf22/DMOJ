// Problem: CCC '15 J1 - Special Day (ccc15j1)
// Problem URL: https://dmoj.ca/problem/ccc15j1
// Submission: 3144253 (https://dmoj.ca/submission/3144253)
// Language: C# (MONOCS)
// Submitted: 2020-11-20T03:28:19+00:00

// CCC '05 J1 - The Cell Sell

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class MainClass 
{
    public static void Main (string[] args) 
    {

        int month = Convert.ToInt32(Console.ReadLine());
        int day = Convert.ToInt32(Console.ReadLine());
        
        if (month == 2 && day == 18)
        {
            Console.WriteLine("Special");
        }
        else if (month == 1 || (month == 2 && day <= 17 ))
        {
            Console.WriteLine("Before");
        }
        else if (month >= 3 || day >= 19)
        {
            Console.WriteLine("After");
        }
        else
        {
            Console.WriteLine("Error");
        }

    }
}