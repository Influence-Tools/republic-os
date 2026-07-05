---
type: Jurisdiction
title: "Oconee County, GA"
classification: county
fips: "13219"
state: "GA"
demographics:
  population: 43551
  population_under_18: 11299
  population_18_64: 24946
  population_65_plus: 7306
  median_household_income: 121217
  poverty_rate: 6.21
  homeownership_rate: 81.27
  unemployment_rate: 3.0
  median_home_value: 461600
  gini_index: 0.457
  vacancy_rate: 4.38
  race_white: 36230
  race_black: 1573
  race_asian: 2043
  race_native: 232
  hispanic: 2538
  bachelors_plus: 23988
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/46"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/house/121"
    rel: in-district
    area_weight: 0.9119
  - to: "us/states/ga/districts/house/120"
    rel: in-district
    area_weight: 0.0872
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Oconee County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43551 |
| Under 18 | 11299 |
| 18–64 | 24946 |
| 65+ | 7306 |
| Median household income | 121217 |
| Poverty rate | 6.21 |
| Homeownership rate | 81.27 |
| Unemployment rate | 3.0 |
| Median home value | 461600 |
| Gini index | 0.457 |
| Vacancy rate | 4.38 |
| White | 36230 |
| Black | 1573 |
| Asian | 2043 |
| Native | 232 |
| Hispanic/Latino | 2538 |
| Bachelor's or higher | 23988 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 46](/us/states/ga/districts/senate/46.md) — 100% (state senate)
- [GA House District 121](/us/states/ga/districts/house/121.md) — 91% (state house)
- [GA House District 120](/us/states/ga/districts/house/120.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
