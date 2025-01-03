library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity demux1to2 is
    Port (
        Sel : in  STD_LOGIC;
        D   : in  STD_LOGIC;
        Y   : out STD_LOGIC_VECTOR (1 downto 0)
    );
end demux1to2;

architecture Behavioral of demux1to2 is
begin
    process (Sel, D)
    begin
        case Sel is
            when '0' => Y(0) <= D;
            when '1' => Y(1) <= D;
            when others => Y(1) <= D;
        end case;
    end process;
end Behavioral;