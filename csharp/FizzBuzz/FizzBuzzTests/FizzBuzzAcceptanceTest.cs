using System;
using System.IO;
using System.Threading.Tasks;
using VerifyXunit;
using Xunit;

namespace FizzBuzz;

public class FizzBuzzAcceptanceTest
{
    [Fact]
    public Task FizzBuzzUpTo100()
    {
        var sw = new StringWriter();
        
        new FizzBuzz().Print(sw);
        
        sw.Flush();
        return Verifier.Verify(sw.ToString());
    }   
}