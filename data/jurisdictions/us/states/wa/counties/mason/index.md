---
type: Jurisdiction
title: "Mason County, WA"
classification: county
fips: "53045"
state: "WA"
demographics:
  population: 67982
  population_under_18: 13273
  population_18_64: 38241
  population_65_plus: 16468
  median_household_income: 83270
  poverty_rate: 12.26
  homeownership_rate: 82.32
  unemployment_rate: 6.57
  median_home_value: 411800
  gini_index: 0.4095
  vacancy_rate: 23.78
  race_white: 52340
  race_black: 709
  race_asian: 665
  race_native: 1578
  hispanic: 8685
  bachelors_plus: 14853
districts:
  - to: "us/states/wa/districts/06"
    rel: in-district
    area_weight: 0.953
  - to: "us/states/wa/districts/senate/35"
    rel: in-district
    area_weight: 0.9496
  - to: "us/states/wa/districts/house/35"
    rel: in-district
    area_weight: 0.9496
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Mason County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67982 |
| Under 18 | 13273 |
| 18–64 | 38241 |
| 65+ | 16468 |
| Median household income | 83270 |
| Poverty rate | 12.26 |
| Homeownership rate | 82.32 |
| Unemployment rate | 6.57 |
| Median home value | 411800 |
| Gini index | 0.4095 |
| Vacancy rate | 23.78 |
| White | 52340 |
| Black | 709 |
| Asian | 665 |
| Native | 1578 |
| Hispanic/Latino | 8685 |
| Bachelor's or higher | 14853 |

## Districts

- [WA-06](/us/states/wa/districts/06.md) — 95% (congressional)
- [WA Senate District 35](/us/states/wa/districts/senate/35.md) — 95% (state senate)
- [WA House District 35](/us/states/wa/districts/house/35.md) — 95% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
