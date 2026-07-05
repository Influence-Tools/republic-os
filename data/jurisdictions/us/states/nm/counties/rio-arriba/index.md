---
type: Jurisdiction
title: "Rio Arriba County, NM"
classification: county
fips: "35039"
state: "NM"
demographics:
  population: 40070
  population_under_18: 9016
  population_18_64: 22312
  population_65_plus: 8742
  median_household_income: 57155
  poverty_rate: 18.24
  homeownership_rate: 80.0
  unemployment_rate: 4.93
  median_home_value: 243700
  gini_index: 0.4557
  vacancy_rate: 21.22
  race_white: 8691
  race_black: 272
  race_asian: 252
  race_native: 6800
  hispanic: 26916
  bachelors_plus: 7681
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/22"
    rel: in-district
    area_weight: 0.5754
  - to: "us/states/nm/districts/senate/5"
    rel: in-district
    area_weight: 0.3952
  - to: "us/states/nm/districts/senate/6"
    rel: in-district
    area_weight: 0.0294
  - to: "us/states/nm/districts/house/41"
    rel: in-district
    area_weight: 0.6451
  - to: "us/states/nm/districts/house/65"
    rel: in-district
    area_weight: 0.3071
  - to: "us/states/nm/districts/house/40"
    rel: in-district
    area_weight: 0.0477
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Rio Arriba County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40070 |
| Under 18 | 9016 |
| 18–64 | 22312 |
| 65+ | 8742 |
| Median household income | 57155 |
| Poverty rate | 18.24 |
| Homeownership rate | 80.0 |
| Unemployment rate | 4.93 |
| Median home value | 243700 |
| Gini index | 0.4557 |
| Vacancy rate | 21.22 |
| White | 8691 |
| Black | 272 |
| Asian | 252 |
| Native | 6800 |
| Hispanic/Latino | 26916 |
| Bachelor's or higher | 7681 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 22](/us/states/nm/districts/senate/22.md) — 58% (state senate)
- [NM Senate District 5](/us/states/nm/districts/senate/5.md) — 40% (state senate)
- [NM Senate District 6](/us/states/nm/districts/senate/6.md) — 3% (state senate)
- [NM House District 41](/us/states/nm/districts/house/41.md) — 65% (state house)
- [NM House District 65](/us/states/nm/districts/house/65.md) — 31% (state house)
- [NM House District 40](/us/states/nm/districts/house/40.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
