// Problem: CCC '15 J2 - Happy or Sad (ccc15j2)
// Problem URL: https://dmoj.ca/problem/ccc15j2
// Submission: 3144316 (https://dmoj.ca/submission/3144316)
// Language: C# (MONOCS)
// Submitted: 2020-11-20T04:18:10+00:00

// Start of C#

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class MainClass 
{
    public static void Main (string[] args) 
    {
        string line = Console.ReadLine();
        
        int happyCounter = 0;
        int sadCounter = 0;
        
        bool stepOne = false;
        bool stepTwo = false;
        bool stepThree = false;
        
        for (int i = 0; i <= line.Length - 1; i++)
        {
            if (line[i] == ':' || line[i] == '-' || line[i] == ')' || line[i] == '(')
            {
                if (line[i] == ':' && stepTwo == false && stepThree == false)
                {
                    stepOne = true;
                }
                else if (line[i] == '-' && stepOne == true && stepThree == false)
                {
                    stepTwo = true;
                }
                else if ((line[i] == ')' || line[i] == '(') && stepOne == true && stepTwo == true)
                {
                    stepOne = false;
                    stepTwo = false;
                    stepThree = false;
                    if (line[i] == '(')
                    {
                        sadCounter++;
                    }
                    else
                    {
                        happyCounter++;
                    }
                }
                else
                {
                    stepOne = false;
                    stepTwo = false;
                    stepThree = false;
                }
            }
            else
            {
                stepOne = false;
                stepTwo = false;
                stepThree = false;
            }
        }
        
        if (sadCounter == 0 && happyCounter == 0)
        {
            Console.WriteLine("none");
        }
        else if (sadCounter == happyCounter)
        {
            Console.WriteLine("unsure");
        }
        else if (sadCounter < happyCounter)
        {
            Console.WriteLine("happy");
        }
        else
        {
            Console.WriteLine("sad");
        }
        
    }
}