library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity mux2to1 is
    Port (
        Sel : in  STD_LOGIC;
        D   : in  STD_LOGIC_VECTOR (1 downto 0);
        Y   : out STD_LOGIC
    );
end mux2to1;

architecture Behavioral of mux2to1 is
begin
    process (Sel, D)
    begin
        case Sel is
            when '0' => Y <= D(0);
            when '1' => Y <= D(1);
            when others => Y <= D(1);
        end case;
    end process;
end Behavioral;