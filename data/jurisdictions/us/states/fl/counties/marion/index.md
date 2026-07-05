---
type: Jurisdiction
title: "Marion County, FL"
classification: county
fips: "12083"
state: "FL"
demographics:
  population: 400078
  population_under_18: 75043
  population_18_64: 210246
  population_65_plus: 114789
  median_household_income: 61010
  poverty_rate: 14.41
  homeownership_rate: 77.47
  unemployment_rate: 4.84
  median_home_value: 243100
  gini_index: 0.4476
  vacancy_rate: 12.43
  race_white: 276476
  race_black: 48446
  race_asian: 7062
  race_native: 1143
  hispanic: 68129
  bachelors_plus: 95072
districts:
  - to: "us/states/fl/districts/06"
    rel: in-district
    area_weight: 0.6049
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.3948
  - to: "us/states/fl/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/fl/districts/house/20"
    rel: in-district
    area_weight: 0.2763
  - to: "us/states/fl/districts/house/27"
    rel: in-district
    area_weight: 0.2606
  - to: "us/states/fl/districts/house/24"
    rel: in-district
    area_weight: 0.1952
  - to: "us/states/fl/districts/house/21"
    rel: in-district
    area_weight: 0.1655
  - to: "us/states/fl/districts/house/23"
    rel: in-district
    area_weight: 0.1023
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Marion County, FL

County jurisdiction — 42 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 400078 |
| Under 18 | 75043 |
| 18–64 | 210246 |
| 65+ | 114789 |
| Median household income | 61010 |
| Poverty rate | 14.41 |
| Homeownership rate | 77.47 |
| Unemployment rate | 4.84 |
| Median home value | 243100 |
| Gini index | 0.4476 |
| Vacancy rate | 12.43 |
| White | 276476 |
| Black | 48446 |
| Asian | 7062 |
| Native | 1143 |
| Hispanic/Latino | 68129 |
| Bachelor's or higher | 95072 |

## Districts

- [FL-06](/us/states/fl/districts/06.md) — 60% (congressional)
- [FL-03](/us/states/fl/districts/03.md) — 39% (congressional)
- [FL Senate District 9](/us/states/fl/districts/senate/9.md) — 100% (state senate)
- [FL House District 20](/us/states/fl/districts/house/20.md) — 28% (state house)
- [FL House District 27](/us/states/fl/districts/house/27.md) — 26% (state house)
- [FL House District 24](/us/states/fl/districts/house/24.md) — 20% (state house)
- [FL House District 21](/us/states/fl/districts/house/21.md) — 17% (state house)
- [FL House District 23](/us/states/fl/districts/house/23.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
