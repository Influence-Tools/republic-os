---
type: Jurisdiction
title: "Fayette County, PA"
classification: county
fips: "42051"
state: "PA"
demographics:
  population: 125997
  population_under_18: 24221
  population_18_64: 73219
  population_65_plus: 28557
  median_household_income: 58236
  poverty_rate: 16.82
  homeownership_rate: 72.39
  unemployment_rate: 6.26
  median_home_value: 143200
  gini_index: 0.4482
  vacancy_rate: 11.22
  race_white: 112746
  race_black: 4932
  race_asian: 582
  race_native: 121
  hispanic: 1822
  bachelors_plus: 23817
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/senate/32"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/house/52"
    rel: in-district
    area_weight: 0.5425
  - to: "us/states/pa/districts/house/51"
    rel: in-district
    area_weight: 0.4571
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Fayette County, PA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 125997 |
| Under 18 | 24221 |
| 18–64 | 73219 |
| 65+ | 28557 |
| Median household income | 58236 |
| Poverty rate | 16.82 |
| Homeownership rate | 72.39 |
| Unemployment rate | 6.26 |
| Median home value | 143200 |
| Gini index | 0.4482 |
| Vacancy rate | 11.22 |
| White | 112746 |
| Black | 4932 |
| Asian | 582 |
| Native | 121 |
| Hispanic/Latino | 1822 |
| Bachelor's or higher | 23817 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 100% (congressional)
- [PA Senate District 32](/us/states/pa/districts/senate/32.md) — 100% (state senate)
- [PA House District 52](/us/states/pa/districts/house/52.md) — 54% (state house)
- [PA House District 51](/us/states/pa/districts/house/51.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
