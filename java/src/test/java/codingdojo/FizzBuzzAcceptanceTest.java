package codingdojo;

import org.approvaltests.Approvals;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

public class FizzBuzzAcceptanceTest {

    @Test
    @DisplayName("FizzBuzz up to 100")
    void fizzBuzzUpTo100() {
        ByteArrayOutputStream bo = new ByteArrayOutputStream();
        var out = new PrintStream(bo);

        new FizzBuzz().print(out);

        Approvals.verify(bo.toString(StandardCharsets.UTF_8));
    }
}
