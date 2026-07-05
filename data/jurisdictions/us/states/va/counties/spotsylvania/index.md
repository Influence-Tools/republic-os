---
type: Jurisdiction
title: "Spotsylvania County, VA"
classification: county
fips: "51177"
state: "VA"
demographics:
  population: 152021
  population_under_18: 40585
  population_18_64: 48098
  population_65_plus: 63338
  median_household_income: 109560
  poverty_rate: 7.16
  homeownership_rate: 78.5
  unemployment_rate: 5.21
  median_home_value: 441700
  gini_index: 0.3869
  vacancy_rate: 7.42
  race_white: 90758
  race_black: 26391
  race_asian: 3849
  race_native: 670
  hispanic: 22446
  bachelors_plus: 54696
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.4723
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.4033
  - to: "us/states/va/districts/senate/27"
    rel: in-district
    area_weight: 0.1242
  - to: "us/states/va/districts/house/63"
    rel: in-district
    area_weight: 0.5557
  - to: "us/states/va/districts/house/66"
    rel: in-district
    area_weight: 0.4286
  - to: "us/states/va/districts/house/65"
    rel: in-district
    area_weight: 0.0152
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Spotsylvania County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 152021 |
| Under 18 | 40585 |
| 18–64 | 48098 |
| 65+ | 63338 |
| Median household income | 109560 |
| Poverty rate | 7.16 |
| Homeownership rate | 78.5 |
| Unemployment rate | 5.21 |
| Median home value | 441700 |
| Gini index | 0.3869 |
| Vacancy rate | 7.42 |
| White | 90758 |
| Black | 26391 |
| Asian | 3849 |
| Native | 670 |
| Hispanic/Latino | 22446 |
| Bachelor's or higher | 54696 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 100% (congressional)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 47% (state senate)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 40% (state senate)
- [VA Senate District 27](/us/states/va/districts/senate/27.md) — 12% (state senate)
- [VA House District 63](/us/states/va/districts/house/63.md) — 56% (state house)
- [VA House District 66](/us/states/va/districts/house/66.md) — 43% (state house)
- [VA House District 65](/us/states/va/districts/house/65.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
