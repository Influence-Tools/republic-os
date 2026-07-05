---
type: Jurisdiction
title: "Somerset County, MD"
classification: county
fips: "24039"
state: "MD"
demographics:
  population: 24822
  population_under_18: 4336
  population_18_64: 16067
  population_65_plus: 4419
  median_household_income: 64943
  poverty_rate: 16.36
  homeownership_rate: 73.12
  unemployment_rate: 7.46
  median_home_value: 173200
  gini_index: 0.4515
  vacancy_rate: 23.61
  race_white: 12896
  race_black: 9623
  race_asian: 185
  race_native: 60
  hispanic: 1144
  bachelors_plus: 4696
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.6047
  - to: "us/states/md/districts/senate/38"
    rel: in-district
    area_weight: 0.5715
  - to: "us/states/md/districts/house/38a"
    rel: in-district
    area_weight: 0.5715
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Somerset County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24822 |
| Under 18 | 4336 |
| 18–64 | 16067 |
| 65+ | 4419 |
| Median household income | 64943 |
| Poverty rate | 16.36 |
| Homeownership rate | 73.12 |
| Unemployment rate | 7.46 |
| Median home value | 173200 |
| Gini index | 0.4515 |
| Vacancy rate | 23.61 |
| White | 12896 |
| Black | 9623 |
| Asian | 185 |
| Native | 60 |
| Hispanic/Latino | 1144 |
| Bachelor's or higher | 4696 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 60% (congressional)
- [MD Senate District 38](/us/states/md/districts/senate/38.md) — 57% (state senate)
- [MD House District 38A](/us/states/md/districts/house/38a.md) — 57% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
