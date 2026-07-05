---
type: Jurisdiction
title: "Kenai Peninsula Borough, AK"
classification: county
fips: "02122"
state: "AK"
demographics:
  population: 60413
  population_under_18: 14505
  population_18_64: 18355
  population_65_plus: 27553
  median_household_income: 80538
  poverty_rate: 11.81
  homeownership_rate: 77.02
  unemployment_rate: 6.99
  median_home_value: 323200
  gini_index: 0.4509
  vacancy_rate: 25.78
  race_white: 47520
  race_black: 364
  race_asian: 1110
  race_native: 3775
  hispanic: 2654
  bachelors_plus: 17215
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.6743
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.3144
  - to: "us/states/ak/districts/senate/d"
    rel: in-district
    area_weight: 0.1794
  - to: "us/states/ak/districts/senate/c"
    rel: in-district
    area_weight: 0.1733
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.3144
  - to: "us/states/ak/districts/house/8"
    rel: in-district
    area_weight: 0.1763
  - to: "us/states/ak/districts/house/6"
    rel: in-district
    area_weight: 0.1054
  - to: "us/states/ak/districts/house/5"
    rel: in-district
    area_weight: 0.0679
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Kenai Peninsula Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60413 |
| Under 18 | 14505 |
| 18–64 | 18355 |
| 65+ | 27553 |
| Median household income | 80538 |
| Poverty rate | 11.81 |
| Homeownership rate | 77.02 |
| Unemployment rate | 6.99 |
| Median home value | 323200 |
| Gini index | 0.4509 |
| Vacancy rate | 25.78 |
| White | 47520 |
| Black | 364 |
| Asian | 1110 |
| Native | 3775 |
| Hispanic/Latino | 2654 |
| Bachelor's or higher | 17215 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 67% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 31% (state senate)
- [AK Senate District D](/us/states/ak/districts/senate/d.md) — 18% (state senate)
- [AK Senate District C](/us/states/ak/districts/senate/c.md) — 17% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 31% (state house)
- [AK House District 8](/us/states/ak/districts/house/8.md) — 18% (state house)
- [AK House District 6](/us/states/ak/districts/house/6.md) — 11% (state house)
- [AK House District 5](/us/states/ak/districts/house/5.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
