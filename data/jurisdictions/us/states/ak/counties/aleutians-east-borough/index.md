---
type: Jurisdiction
title: "Aleutians East Borough, AK"
classification: county
fips: "02013"
state: "AK"
demographics:
  population: 3491
  population_under_18: 540
  population_18_64: 1389
  population_65_plus: 1562
  median_household_income: 65365
  poverty_rate: 13.22
  homeownership_rate: 64.21
  unemployment_rate: 8.35
  median_home_value: 135500
  gini_index: 0.4008
  vacancy_rate: 16.06
  race_white: 606
  race_black: 108
  race_asian: 664
  race_native: 1395
  hispanic: 303
  bachelors_plus: 630
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.4954
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.4774
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.4774
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Aleutians East Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3491 |
| Under 18 | 540 |
| 18–64 | 1389 |
| 65+ | 1562 |
| Median household income | 65365 |
| Poverty rate | 13.22 |
| Homeownership rate | 64.21 |
| Unemployment rate | 8.35 |
| Median home value | 135500 |
| Gini index | 0.4008 |
| Vacancy rate | 16.06 |
| White | 606 |
| Black | 108 |
| Asian | 664 |
| Native | 1395 |
| Hispanic/Latino | 303 |
| Bachelor's or higher | 630 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 50% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 48% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
