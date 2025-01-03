library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity mux4to1 is
    Port (
        Sel : in  STD_LOGIC_VECTOR (1 downto 0);
        D   : in  STD_LOGIC_VECTOR (3 downto 0);
        Y   : out STD_LOGIC
    );
end mux4to1;

architecture Behavioral of mux4to1 is
begin
    process (Sel, D)
    begin
        case Sel is
            when "00" => Y <= D(0);
            when "01" => Y <= D(1);
            when "10" => Y <= D(2);
            when "11" => Y <= D(3);
            when others => Y <= D(3);
        end case;
    end process;
end Behavioral;