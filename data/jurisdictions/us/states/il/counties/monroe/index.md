---
type: Jurisdiction
title: "Monroe County, IL"
classification: county
fips: "17133"
state: "IL"
demographics:
  population: 35036
  population_under_18: 7651
  population_18_64: 20472
  population_65_plus: 6913
  median_household_income: 102880
  poverty_rate: 5.02
  homeownership_rate: 84.66
  unemployment_rate: 1.92
  median_home_value: 282100
  gini_index: 0.4032
  vacancy_rate: 6.15
  race_white: 33641
  race_black: 207
  race_asian: 209
  race_native: 34
  hispanic: 683
  bachelors_plus: 13121
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Monroe County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35036 |
| Under 18 | 7651 |
| 18–64 | 20472 |
| 65+ | 6913 |
| Median household income | 102880 |
| Poverty rate | 5.02 |
| Homeownership rate | 84.66 |
| Unemployment rate | 1.92 |
| Median home value | 282100 |
| Gini index | 0.4032 |
| Vacancy rate | 6.15 |
| White | 33641 |
| Black | 207 |
| Asian | 209 |
| Native | 34 |
| Hispanic/Latino | 683 |
| Bachelor's or higher | 13121 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 115](/us/states/il/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
