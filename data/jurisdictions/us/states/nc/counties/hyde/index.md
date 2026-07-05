---
type: Jurisdiction
title: "Hyde County, NC"
classification: county
fips: "37095"
state: "NC"
demographics:
  population: 4592
  population_under_18: 826
  population_18_64: 2864
  population_65_plus: 902
  median_household_income: 53713
  poverty_rate: 22.18
  homeownership_rate: 71.94
  unemployment_rate: 2.49
  median_home_value: 124000
  gini_index: 0.4052
  vacancy_rate: 34.32
  race_white: 2649
  race_black: 1128
  race_asian: 0
  race_native: 67
  hispanic: 464
  bachelors_plus: 675
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.5155
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.4832
  - to: "us/states/nc/districts/house/79"
    rel: in-district
    area_weight: 0.4832
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Hyde County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4592 |
| Under 18 | 826 |
| 18–64 | 2864 |
| 65+ | 902 |
| Median household income | 53713 |
| Poverty rate | 22.18 |
| Homeownership rate | 71.94 |
| Unemployment rate | 2.49 |
| Median home value | 124000 |
| Gini index | 0.4052 |
| Vacancy rate | 34.32 |
| White | 2649 |
| Black | 1128 |
| Asian | 0 |
| Native | 67 |
| Hispanic/Latino | 464 |
| Bachelor's or higher | 675 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 52% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 48% (state senate)
- [NC House District 79](/us/states/nc/districts/house/79.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
