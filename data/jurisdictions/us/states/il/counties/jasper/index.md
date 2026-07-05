---
type: Jurisdiction
title: "Jasper County, IL"
classification: county
fips: "17079"
state: "IL"
demographics:
  population: 9180
  population_under_18: 2069
  population_18_64: 5185
  population_65_plus: 1926
  median_household_income: 74755
  poverty_rate: 11.06
  homeownership_rate: 85.2
  unemployment_rate: 4.18
  median_home_value: 125500
  gini_index: 0.4056
  vacancy_rate: 11.24
  race_white: 8892
  race_black: 7
  race_asian: 12
  race_native: 0
  hispanic: 123
  bachelors_plus: 1813
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Jasper County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9180 |
| Under 18 | 2069 |
| 18–64 | 5185 |
| 65+ | 1926 |
| Median household income | 74755 |
| Poverty rate | 11.06 |
| Homeownership rate | 85.2 |
| Unemployment rate | 4.18 |
| Median home value | 125500 |
| Gini index | 0.4056 |
| Vacancy rate | 11.24 |
| White | 8892 |
| Black | 7 |
| Asian | 12 |
| Native | 0 |
| Hispanic/Latino | 123 |
| Bachelor's or higher | 1813 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
