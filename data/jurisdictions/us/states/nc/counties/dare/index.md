---
type: Jurisdiction
title: "Dare County, NC"
classification: county
fips: "37055"
state: "NC"
demographics:
  population: 37875
  population_under_18: 6771
  population_18_64: 21541
  population_65_plus: 9563
  median_household_income: 88994
  poverty_rate: 6.62
  homeownership_rate: 78.42
  unemployment_rate: 5.94
  median_home_value: 460400
  gini_index: 0.4915
  vacancy_rate: 52.28
  race_white: 32699
  race_black: 964
  race_asian: 185
  race_native: 47
  hispanic: 2788
  bachelors_plus: 16283
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.2927
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.2651
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.2131
  - to: "us/states/nc/districts/house/79"
    rel: in-district
    area_weight: 0.052
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Dare County, NC

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37875 |
| Under 18 | 6771 |
| 18–64 | 21541 |
| 65+ | 9563 |
| Median household income | 88994 |
| Poverty rate | 6.62 |
| Homeownership rate | 78.42 |
| Unemployment rate | 5.94 |
| Median home value | 460400 |
| Gini index | 0.4915 |
| Vacancy rate | 52.28 |
| White | 32699 |
| Black | 964 |
| Asian | 185 |
| Native | 47 |
| Hispanic/Latino | 2788 |
| Bachelor's or higher | 16283 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 29% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 27% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 21% (state house)
- [NC House District 79](/us/states/nc/districts/house/79.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
