package ecsc24;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.spec.KeySpec;
import java.util.Base64;
import java.util.Map;
import java.util.UUID;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String seed = new String(new char[11]).replace("\0", String.valueOf(Character.MAX_VALUE));
        String encryptedFlag = "INNb6+40E6zZ2Sp6pnpwy/5uB6Lte0dWH4721kv2xLl/EiE+AsYAdx16GHln2CV9Vxya+g7QFQWmkEq3sHvTOA==";
        
        Decryptor decryptor = new Decryptor();
        String decryptedText = decryptor.decrypt(encryptedFlag, seed);
        System.out.println(decryptedText);
    }
}

class Decryptor {
    private final Map<C, String> secrets = IntStream.range(Character.MIN_VALUE, Character.MAX_VALUE)
            .mapToObj(C::new)
            .collect(Collectors.toMap(
                    Function.identity(),
                    c -> UUID.randomUUID().toString()
            ));

    String generateRandomPassword(String userInput) {
        return userInput.chars()
                .mapToObj(i -> (char) i)
                .map(C::new)
                .map(secrets::get)
                .collect(Collectors.joining());
    }

    SecretKey getKeyFromPassword(String password) throws Exception {
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        KeySpec spec = new PBEKeySpec(password.toCharArray(), "Why so salty?".getBytes(), 65536, 256);
        return new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");
    }

    public String decrypt(String encryptedText, String userInput) throws Exception {
        SecretKey key = getKeyFromPassword(generateRandomPassword(userInput));
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] cipherText = Base64.getDecoder().decode(encryptedText);
        byte[] plainText = cipher.doFinal(cipherText);
        return new String(plainText);
    }
}

class C {
    private final Integer index;

    public C(Integer index) {
        this.index = index;
    }

    public C(Character c) {
        this.index = (int) c;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        C a = (C) o;
        return index.equals(a.index);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(index);
    }
}
