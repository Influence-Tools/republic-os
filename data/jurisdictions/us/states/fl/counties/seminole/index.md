---
type: Jurisdiction
title: "Seminole County, FL"
classification: county
fips: "12117"
state: "FL"
demographics:
  population: 481470
  population_under_18: 98915
  population_18_64: 302503
  population_65_plus: 80052
  median_household_income: 85761
  poverty_rate: 9.03
  homeownership_rate: 66.2
  unemployment_rate: 4.15
  median_home_value: 386900
  gini_index: 0.4426
  vacancy_rate: 6.17
  race_white: 284854
  race_black: 56660
  race_asian: 26087
  race_native: 934
  hispanic: 115251
  bachelors_plus: 197645
districts:
  - to: "us/states/fl/districts/07"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/fl/districts/senate/10"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/fl/districts/house/36"
    rel: in-district
    area_weight: 0.5061
  - to: "us/states/fl/districts/house/37"
    rel: in-district
    area_weight: 0.2554
  - to: "us/states/fl/districts/house/38"
    rel: in-district
    area_weight: 0.1527
  - to: "us/states/fl/districts/house/39"
    rel: in-district
    area_weight: 0.0854
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Seminole County, FL

County jurisdiction — 52 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 481470 |
| Under 18 | 98915 |
| 18–64 | 302503 |
| 65+ | 80052 |
| Median household income | 85761 |
| Poverty rate | 9.03 |
| Homeownership rate | 66.2 |
| Unemployment rate | 4.15 |
| Median home value | 386900 |
| Gini index | 0.4426 |
| Vacancy rate | 6.17 |
| White | 284854 |
| Black | 56660 |
| Asian | 26087 |
| Native | 934 |
| Hispanic/Latino | 115251 |
| Bachelor's or higher | 197645 |

## Districts

- [FL-07](/us/states/fl/districts/07.md) — 100% (congressional)
- [FL Senate District 10](/us/states/fl/districts/senate/10.md) — 100% (state senate)
- [FL House District 36](/us/states/fl/districts/house/36.md) — 51% (state house)
- [FL House District 37](/us/states/fl/districts/house/37.md) — 26% (state house)
- [FL House District 38](/us/states/fl/districts/house/38.md) — 15% (state house)
- [FL House District 39](/us/states/fl/districts/house/39.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
