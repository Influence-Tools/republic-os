---
type: Jurisdiction
title: "San Miguel County, NM"
classification: county
fips: "35047"
state: "NM"
demographics:
  population: 26850
  population_under_18: 4528
  population_18_64: 15454
  population_65_plus: 6868
  median_household_income: 49431
  poverty_rate: 24.41
  homeownership_rate: 73.07
  unemployment_rate: 4.79
  median_home_value: 188500
  gini_index: 0.4725
  vacancy_rate: 19.75
  race_white: 10927
  race_black: 463
  race_asian: 97
  race_native: 620
  hispanic: 20192
  bachelors_plus: 7511
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/8"
    rel: in-district
    area_weight: 0.8038
  - to: "us/states/nm/districts/senate/39"
    rel: in-district
    area_weight: 0.1962
  - to: "us/states/nm/districts/house/70"
    rel: in-district
    area_weight: 0.7044
  - to: "us/states/nm/districts/house/67"
    rel: in-district
    area_weight: 0.2257
  - to: "us/states/nm/districts/house/40"
    rel: in-district
    area_weight: 0.0596
  - to: "us/states/nm/districts/house/63"
    rel: in-district
    area_weight: 0.0102
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# San Miguel County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26850 |
| Under 18 | 4528 |
| 18–64 | 15454 |
| 65+ | 6868 |
| Median household income | 49431 |
| Poverty rate | 24.41 |
| Homeownership rate | 73.07 |
| Unemployment rate | 4.79 |
| Median home value | 188500 |
| Gini index | 0.4725 |
| Vacancy rate | 19.75 |
| White | 10927 |
| Black | 463 |
| Asian | 97 |
| Native | 620 |
| Hispanic/Latino | 20192 |
| Bachelor's or higher | 7511 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 8](/us/states/nm/districts/senate/8.md) — 80% (state senate)
- [NM Senate District 39](/us/states/nm/districts/senate/39.md) — 20% (state senate)
- [NM House District 70](/us/states/nm/districts/house/70.md) — 70% (state house)
- [NM House District 67](/us/states/nm/districts/house/67.md) — 23% (state house)
- [NM House District 40](/us/states/nm/districts/house/40.md) — 6% (state house)
- [NM House District 63](/us/states/nm/districts/house/63.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
