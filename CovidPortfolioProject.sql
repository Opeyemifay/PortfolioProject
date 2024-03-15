
/* Covid 19 Data Exploration

Skills Used: Joins, CTEs, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data types.

*/


select *
from PortfolioProject..CovidDeaths
where continent is not null
order by 3, 4


--Selecting Data to start with

select location, date, total_cases, new_cases, total_deaths, population
from PortfolioProject..CovidDeaths
where continent is not null
order by 1,2


--Total Cases  vs Total Deaths
--Shows the likelihood of dying, if you contract covid in Nigeria.

select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from PortfolioProject..CovidDeaths
where location = 'Nigeria'
and continent is not null
order by location, date


--Total cases vs Population
-- Shows what percentage of population is infected with Covid in Nigeria

select location, date, population,total_cases, (total_cases/population)*100 as PercentPopulationInfected
from PortfolioProject..CovidDeaths
where location = 'Nigeria'
order by location, date


--Countries with highest infection rate compared to population

select location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentPopulationInfected
from PortfolioProject..CovidDeaths
--where location = 'Nigeria'
group by location, population
order by PercentPopulationInfected DESC


--Countries With Highest Death Count per Population


select location, MAX(CAST(total_deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
--where location = 'Nigeria'
where continent is not null
group by location
order by TotalDeathCount DESC


--By Continent
--Showing Continents with Highest Death Count per Population

select continent, MAX(CAST(total_deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
--where location = 'Nigeria'
where continent is not null
group by continent
order by TotalDeathCount DESC


--Global Numbers


select SUM(new_cases) as total_cases, SUM(CAST(new_deaths as int)) as total_deaths, SUM(CAST(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
from PortfolioProject..CovidDeaths
--where location = 'Nigeria'
where continent is not null
--group by location
order by 1,2

--Total Populations vs Total Vaccines
--Shows Percentage of Population that have received at least one Covid Vaccine

select dth.continent, dth.location, dth.date, dth.population, vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dth.location Order by dth.location, dth.date) as RollingPeopleVaccinated
--,(RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dth
Join PortfolioProject..CovidVaccinations vac
On dth.location = vac.location
and dth.date = vac.date
where dth.continent is not null
order by 2,3


--Using CTE to perform Calculation on Partition By in previous query


With PopvsVac(Continent, Location, Date, Population, New_Vaccination, RollingPeopleVaccinated)
as
(
select dth.continent, dth.location, dth.date, dth.population, vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dth.location Order by dth.location, dth.date) as RollingPeopleVaccinated
--,(RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dth
Join PortfolioProject..CovidVaccinations vac
On dth.location = vac.location
and dth.date = vac.date
where dth.continent is not null
--order by 2,3
)
select *, (RollingPeopleVaccinated/Population)*100
from PopvsVac



--Using Temp Table to perform Calculation on Partition By in previous query


DROP TABLE if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
Insert into #PercentPopulationVaccinated
select dth.continent, dth.location, dth.date, dth.population, vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dth.location Order by dth.location, dth.date) as RollingPeopleVaccinated
--,(RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dth
Join PortfolioProject..CovidVaccinations vac
On dth.location = vac.location
and dth.date = vac.date
where dth.continent is not null
--order by 2,3

select *, (RollingPeopleVaccinated/Population)*100
from #PercentPopulationVaccinated



--Creating View to store data for later visualizations


CREATE VIEW PercentPopulationVaccinated as
select dth.continent, dth.location, dth.date, dth.population, vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dth.location Order by dth.location, dth.date) as RollingPeopleVaccinated
--,(RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dth
Join PortfolioProject..CovidVaccinations vac
On dth.location = vac.location
and dth.date = vac.date
where dth.continent is not null


