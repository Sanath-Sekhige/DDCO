library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity demux1to8 is
    Port (
        Sel : in  STD_LOGIC_VECTOR (2 downto 0);
        D   : in  STD_LOGIC;
        Y   : out STD_LOGIC_VECTOR (7 downto 0)
    );
end demux1to8;

architecture Behavioral of demux1to8 is
begin
    process (Sel, D)
    begin
        case Sel is
            when "000" => Y(0) <= D;
            when "001" => Y(1) <= D;
			when "010" => Y(2) <= D;
			when "011" => Y(3) <= D;
			when "100" => Y(4) <= D;
			when "101" => Y(5) <= D;
			when "110" => Y(6) <= D;
			when "111" => Y(7) <= D;
            when others => Y(7) <= D;
        end case;
    end process;
end Behavioral;