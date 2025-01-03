library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity demux1to4 is
    Port (
        Sel : in  STD_LOGIC_VECTOR (1 downto 0);
        D   : in  STD_LOGIC;
        Y   : out STD_LOGIC_VECTOR (3 downto 0)
    );
end demux1to4;

architecture Behavioral of demux1to4 is
begin
    process (Sel, D)
    begin
        case Sel is
            when "00" => Y(0) <= D;
            when "01" => Y(1) <= D;
			when "10" => Y(2) <= D;
			when "11" => Y(3) <= D;
            when others => Y(3) <= D;
        end case;
    end process;
end Behavioral;