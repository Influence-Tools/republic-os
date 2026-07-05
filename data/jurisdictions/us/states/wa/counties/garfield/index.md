---
type: Jurisdiction
title: "Garfield County, WA"
classification: county
fips: "53023"
state: "WA"
demographics:
  population: 2353
  population_under_18: 440
  population_18_64: 1300
  population_65_plus: 613
  median_household_income: 64884
  poverty_rate: 11.99
  homeownership_rate: 76.92
  unemployment_rate: 6.27
  median_home_value: 239200
  gini_index: 0.4098
  vacancy_rate: 15.56
  race_white: 2092
  race_black: 19
  race_asian: 49
  race_native: 1
  hispanic: 117
  bachelors_plus: 766
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Garfield County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2353 |
| Under 18 | 440 |
| 18–64 | 1300 |
| 65+ | 613 |
| Median household income | 64884 |
| Poverty rate | 11.99 |
| Homeownership rate | 76.92 |
| Unemployment rate | 6.27 |
| Median home value | 239200 |
| Gini index | 0.4098 |
| Vacancy rate | 15.56 |
| White | 2092 |
| Black | 19 |
| Asian | 49 |
| Native | 1 |
| Hispanic/Latino | 117 |
| Bachelor's or higher | 766 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 100% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
