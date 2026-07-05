---
type: Jurisdiction
title: "San Juan County, WA"
classification: county
fips: "53055"
state: "WA"
demographics:
  population: 18478
  population_under_18: 2323
  population_18_64: 9499
  population_65_plus: 6656
  median_household_income: 84800
  poverty_rate: 11.34
  homeownership_rate: 77.99
  unemployment_rate: 3.66
  median_home_value: 799200
  gini_index: 0.532
  vacancy_rate: 35.56
  race_white: 16035
  race_black: 45
  race_asian: 248
  race_native: 111
  hispanic: 1409
  bachelors_plus: 11868
districts:
  - to: "us/states/wa/districts/02"
    rel: in-district
    area_weight: 0.4132
  - to: "us/states/wa/districts/senate/40"
    rel: in-district
    area_weight: 0.3095
  - to: "us/states/wa/districts/house/40"
    rel: in-district
    area_weight: 0.3095
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# San Juan County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18478 |
| Under 18 | 2323 |
| 18–64 | 9499 |
| 65+ | 6656 |
| Median household income | 84800 |
| Poverty rate | 11.34 |
| Homeownership rate | 77.99 |
| Unemployment rate | 3.66 |
| Median home value | 799200 |
| Gini index | 0.532 |
| Vacancy rate | 35.56 |
| White | 16035 |
| Black | 45 |
| Asian | 248 |
| Native | 111 |
| Hispanic/Latino | 1409 |
| Bachelor's or higher | 11868 |

## Districts

- [WA-02](/us/states/wa/districts/02.md) — 41% (congressional)
- [WA Senate District 40](/us/states/wa/districts/senate/40.md) — 31% (state senate)
- [WA House District 40](/us/states/wa/districts/house/40.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
