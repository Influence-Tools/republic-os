---
type: Jurisdiction
title: "Cibola County, NM"
classification: county
fips: "35006"
state: "NM"
demographics:
  population: 26845
  population_under_18: 6233
  population_18_64: 15731
  population_65_plus: 4881
  median_household_income: 50759
  poverty_rate: 28.4
  homeownership_rate: 76.09
  unemployment_rate: 10.5
  median_home_value: 125400
  gini_index: 0.4589
  vacancy_rate: 24.32
  race_white: 8141
  race_black: 522
  race_asian: 211
  race_native: 12283
  hispanic: 8826
  bachelors_plus: 4573
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/30"
    rel: in-district
    area_weight: 0.6872
  - to: "us/states/nm/districts/senate/4"
    rel: in-district
    area_weight: 0.3127
  - to: "us/states/nm/districts/house/6"
    rel: in-district
    area_weight: 0.5546
  - to: "us/states/nm/districts/house/69"
    rel: in-district
    area_weight: 0.4454
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Cibola County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26845 |
| Under 18 | 6233 |
| 18–64 | 15731 |
| 65+ | 4881 |
| Median household income | 50759 |
| Poverty rate | 28.4 |
| Homeownership rate | 76.09 |
| Unemployment rate | 10.5 |
| Median home value | 125400 |
| Gini index | 0.4589 |
| Vacancy rate | 24.32 |
| White | 8141 |
| Black | 522 |
| Asian | 211 |
| Native | 12283 |
| Hispanic/Latino | 8826 |
| Bachelor's or higher | 4573 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 30](/us/states/nm/districts/senate/30.md) — 69% (state senate)
- [NM Senate District 4](/us/states/nm/districts/senate/4.md) — 31% (state senate)
- [NM House District 6](/us/states/nm/districts/house/6.md) — 55% (state house)
- [NM House District 69](/us/states/nm/districts/house/69.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
