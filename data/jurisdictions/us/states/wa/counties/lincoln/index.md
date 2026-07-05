---
type: Jurisdiction
title: "Lincoln County, WA"
classification: county
fips: "53043"
state: "WA"
demographics:
  population: 11489
  population_under_18: 2505
  population_18_64: 5972
  population_65_plus: 3012
  median_household_income: 71512
  poverty_rate: 12.46
  homeownership_rate: 80.37
  unemployment_rate: 7.77
  median_home_value: 292800
  gini_index: 0.4454
  vacancy_rate: 18.55
  race_white: 10353
  race_black: 68
  race_asian: 54
  race_native: 218
  hispanic: 477
  bachelors_plus: 2630
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9997
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

# Lincoln County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11489 |
| Under 18 | 2505 |
| 18–64 | 5972 |
| 65+ | 3012 |
| Median household income | 71512 |
| Poverty rate | 12.46 |
| Homeownership rate | 80.37 |
| Unemployment rate | 7.77 |
| Median home value | 292800 |
| Gini index | 0.4454 |
| Vacancy rate | 18.55 |
| White | 10353 |
| Black | 68 |
| Asian | 54 |
| Native | 218 |
| Hispanic/Latino | 477 |
| Bachelor's or higher | 2630 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 100% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
