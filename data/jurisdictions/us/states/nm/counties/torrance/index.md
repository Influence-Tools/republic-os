---
type: Jurisdiction
title: "Torrance County, NM"
classification: county
fips: "35057"
state: "NM"
demographics:
  population: 15490
  population_under_18: 3134
  population_18_64: 8868
  population_65_plus: 3488
  median_household_income: 57842
  poverty_rate: 18.27
  homeownership_rate: 81.74
  unemployment_rate: 9.03
  median_home_value: 159700
  gini_index: 0.4563
  vacancy_rate: 17.02
  race_white: 9521
  race_black: 384
  race_asian: 37
  race_native: 488
  hispanic: 6696
  bachelors_plus: 2375
districts:
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/39"
    rel: in-district
    area_weight: 0.9236
  - to: "us/states/nm/districts/senate/19"
    rel: in-district
    area_weight: 0.0763
  - to: "us/states/nm/districts/house/70"
    rel: in-district
    area_weight: 0.5304
  - to: "us/states/nm/districts/house/22"
    rel: in-district
    area_weight: 0.4695
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Torrance County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15490 |
| Under 18 | 3134 |
| 18–64 | 8868 |
| 65+ | 3488 |
| Median household income | 57842 |
| Poverty rate | 18.27 |
| Homeownership rate | 81.74 |
| Unemployment rate | 9.03 |
| Median home value | 159700 |
| Gini index | 0.4563 |
| Vacancy rate | 17.02 |
| White | 9521 |
| Black | 384 |
| Asian | 37 |
| Native | 488 |
| Hispanic/Latino | 6696 |
| Bachelor's or higher | 2375 |

## Districts

- [NM-01](/us/states/nm/districts/01.md) — 100% (congressional)
- [NM Senate District 39](/us/states/nm/districts/senate/39.md) — 92% (state senate)
- [NM Senate District 19](/us/states/nm/districts/senate/19.md) — 8% (state senate)
- [NM House District 70](/us/states/nm/districts/house/70.md) — 53% (state house)
- [NM House District 22](/us/states/nm/districts/house/22.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
